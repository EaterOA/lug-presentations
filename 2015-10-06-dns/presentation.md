Presentation
===

Go through slides until demo.

    dig linux.ucla.edu

Lots of junk, explain A record and different types of records in slides. Maybe
mention interesting records like SPF.

Cut out the junk:

    dig +noall +stats +answer linux.ucla.edu

Point out the SERVER field; that's the router (recursive resolver / cacher).

Continue w/ slides and draw diagram of resolution process.
