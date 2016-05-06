#!/bin/bash

from="Paul Eggert <eggert@cs.ucla.edu>"
to="duperduper@ucla.edu"
subject="COM SCI 130: Midterm grades"
body=$(cat <<EOF
Dear Class,

The midterms have been graded. Here are the statistics:

High: 10/100
Low: -10/100
Mean: 0/100

The overall class average grade is F-. This is better than I expected. Please
continue the good work.


Thank you,

Paul Eggert
EOF
)

mail -s "$subject" -aFrom:"$from" "$to" <<< "$body"
