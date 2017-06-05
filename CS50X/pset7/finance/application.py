from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    """Display a user's current assets"""
    
    # Store assets and total 
    assets = []
    total = 0
    
    # Retrieve rows with user symbols and sum of shares grouped
    rows = db.execute("SELECT symbol, sum(shares) as shares FROM transactions WHERE id=:uid GROUP BY symbol", uid=session['user_id'])
    
    for row in rows:
        
        # Ensure user owns shares of stock
        if row['shares'] != 0:
            
            stock = lookup(row['symbol'])
            row['name'] = stock['name']
            row['price'] = usd(stock['price'])
            
            # Calculate current value of shares
            amount = stock['price'] * row['shares']
            total += amount
            row['total'] = usd(amount)
            assets.append(row)
        
    # Current cash user owns
    cash = db.execute("SELECT cash FROM users WHERE id=:uid", uid=session['user_id'])
    assets.append({'symbol': 'CASH', 'total': usd(cash[0]['cash']), 'price': '', 'name': '', 'shares': '' })
    
    # Calculate total value of assets
    total += cash[0]['cash']
    
    # Return index file with assets and total cash as parameters
    return render_template("index.html", rows=assets, total=usd(total))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    
    # Return page to buy shares
    if request.method == "GET":
        return render_template("buy.html")
    
    # Form was submitted
    elif request.method == "POST":
        
        # Empty symbol input check
        if not request.form.get("symbol"):
            return apology("Missing Symbol")
        
        # Lookup stock information
        stock = lookup(request.form.get("symbol"))
        name = stock['name']
        symbol = stock['symbol']
        price = stock['price']
        
        # Symbol didn't exist
        if stock == None:
            return apology("Invalid Symbol")
        
        # Shares form input
        shares = request.form.get("shares")
        
        # Empty shares input
        if not request.form.get("shares"):
            return apology("Missing shares")
            
        # Check if input contained digits only
        if not (shares.isdigit()):
            return apology("Only Numbers Allowed")

        # Convert shares to int
        shares = int(shares)
        
        # Check if shares is non-negative
        if shares < 0:
            return apology("Negative shares not allowed")
        
        # Return user's current cash
        cash = db.execute("SELECT cash FROM users WHERE id=:uid", uid=session['user_id'])
        
        
        # Calculate purchase amount
        purchase = shares * price
        
        # Check if user has enough cash
        if (purchase > cash[0]['cash']):
            return apology("Not Enough Cash!")
        else:
            
            # Enter transaction history
            db.execute("INSERT INTO transactions (id, symbol, shares, price) VALUES \
                    (:uid, :symbol, :shares, :price)", uid = session['user_id'], \
                    symbol=symbol, shares = shares, price = price)
            
            # Update users cash
            db.execute("UPDATE users SET cash=:cash WHERE id=:uid",\
                        cash = cash[0]['cash'] - purchase, uid=session['user_id'])
        
        flash("Bought!")                
        return redirect(url_for("index"))
        
@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    rows = db.execute("SELECT * FROM transactions WHERE id=:uid", uid=session['user_id'])
    return render_template("history.html", rows=rows)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    
    # return page to request quote
    if request.method == "GET":
        return render_template("quote.html")
        
    # if user submitted quote
    elif request.method == "POST":
        
        # Lookup symbol sent from form request
        stock = lookup(request.form.get("symbol"))
        
        # Ensure stock exists
        if stock:
            
            # Save stock information
            name = stock['name']
            symbol = stock['symbol']
            price = stock['price']        
        
            # Return quote information
            return render_template("quoted.html", name=name, symbol=symbol, price=usd(price))
        
        # Stock doesnt exist
        else:
            return apology("Invalid symbol")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    
    # if user submitted form (registration page)
    if request.method == "POST":
        
        # retrieve form fields info
        username = request.form.get("username")
        password = request.form.get("password")
        checkPass = request.form.get("passwordCheck")
        
        # ensure username was submitted
        if not username:
            return apology("Username is blank")
        
        # ensure password fields were submitted
        elif not password or not checkPass:
            return apology("Password field left blank")
            
        # ensure both password fields are same
        elif (password != checkPass):
            return apology("Passwords do not match")
        
        # create password hash
        hashpwd = pwd_context.hash(password)
        
        # Add new user to database
        result = db.execute("INSERT INTO users (username, hash) VALUES (:name, :hashpwd)", name=username, hashpwd=hashpwd)
        
        # Check if username exists
        if not result:
            return apology("Username already exists")
        
        # Get user ID and store session
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]
        
        # Redirect user to index page instantly logging them in and flash message
        flash("Registered!")
        return redirect(url_for("index"))
    
    # Return registration page if accessed via GET    
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    
    # Return page to sell shares
    if request.method == "GET":
        return render_template("sell.html")
    
    # Form was submitted
    elif request.method == "POST":
        
        # Get stock and symbol information
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        name = stock['name']
        price = stock['price']
        
        # Empty symbol input check
        if not symbol:
            return apology("Missing Symbol")
        
        # Check if symbol exists
        if stock == None:
            return apology("Symbol doesn't exist")
        
        # Check if user owns shares of stock
        rows = db.execute("SELECT * FROM transactions WHERE symbol=:symbol AND id=:uid",\
                    symbol=symbol, uid=session['user_id'])
        if len(rows) == 0:
            return apology("Not owned")
        
        
        shares = request.form.get("shares")
        
        # Empty shares input check
        if not shares:
            return apology("Missing shares field")
        
        # Negative shares and integer characters input check
        if (int(shares) < 0):
            return apology("Negative shares not allowed")
            
        if not (shares.isdigit()):
            return apology("Only Numbers allowed")
        
        
        shares = int(shares)
        
        # Verify the user has enough shares to sell
        heldShares = 0
        
        for row in rows:
            heldShares += row['shares']
        if shares > heldShares:
            return apology("Too many shares")
        
        else:
            sell = shares * price
            
            # Retreive current cash amount
            cash = db.execute("SELECT cash FROM users WHERE id=:uid", uid=session['user_id'])
            
            # Insert transaction
            db.execute("INSERT INTO transactions(id, symbol, shares, price) VALUES \
                    (:uid, :symbol, :shares, :price)", uid = session['user_id'], \
                    symbol = symbol, shares = -shares, price = price)
            
            # Update users cash field
            db.execute("UPDATE users SET cash=:cash WHERE id=:uid",
                        cash = cash[0]['cash'] + sell, uid=session['user_id'])
        
        # Redirect user to homepage and flash message
        flash("Sold!")
        return redirect(url_for("index"))
