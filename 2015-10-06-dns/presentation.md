Preparation
===

* start gotty server
* start python http.server
* start bind container
  * service bind9 start

Confirm that all of the above works

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

Demo with dig trace:

    dig linux.ucla.edu +trace

Demo with bind9.

    dig www.wikipedia.org @<ip of container>

Switch to container view. Go through named.conf and db.custom.

    dig nyaa.moe @<ip of container>

Change db.custom, restart service.

    dig nyaa.moe @<ip of container>

Change recursion all to none, restart service.

    dig www.wikipedia.org @<ip of container>

Go back to slides to talk about reverse DNS. Go back to named.conf to talk
about reverse zone.

    dig -x 172.17.0.1 @<ip of container>

Go back to slides to talk about glue records

    dig linux.ucla.edu +trace +additional
