/* Name: helper.c
   Author: Robin Goyal
   Last-Modified: January 30, 2018
   Purpose: Helper functions for music problem set
*/

#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int numerator = atoi(strtok(fraction, "/"));
    int denominator = atoi(strtok(NULL, "/"));

    // Calculate number of eights in fraction
    int eighths = (8 / denominator) * numerator;

    return eighths;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    int note_len = strlen(note);

    // Parse octave number from note
    int octave = note[note_len - 1] - '0';

    // Parse letter information from note
    char letter[3];
    strncpy(letter, note, note_len - 1);
    letter[note_len - 1] = '\0';

    // Index of note to calculate relative distance
    int note_index = calculate_index(letter);

    // Index of A4 (standard pitch)
    int std_pitch_index = 9;

    // Frequency equation is f = 440 * 2 ** (n / 12) where n is the number of semitones
    float semitones = (note_index - std_pitch_index) + (octave - 4) * 12;
    int frequency = round(440 * pow(2, semitones / 12));

    return frequency;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{

    // Returns True if string is empty
    return (strcmp(s, "") == 0);
}


// Returns index of note
int calculate_index(string letter)
{
    string NOTES[] = {"C", "C#", "D", "D#", "E", "F",
                      "F#", "G", "G#", "A", "A#", "B"
                     };

    // Return index of note in NOTES accounting for flats
    int note_index;
    for (int i = 0, n = sizeof(NOTES) / sizeof(string); i < n; i++)
    {
        // Letter is the same
        if (letter[0] == NOTES[i][0])
        {
            // Account for accidentals (#'s or b's)
            if (letter[1] == '#')
            {
                note_index = i + 1;
            }
            else if (letter[1] == 'b')
            {
                note_index = i - 1;
            }
            else
            {
                note_index = i;
            }

            return note_index;
        }
    }

    // The note doesn't exist in array
    return -1;
}
