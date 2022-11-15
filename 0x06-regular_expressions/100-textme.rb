#!/usr/bin/env ruby
#  exercise was prepared by Guillaume Plessis, VP of Infrastructure at TextMe
#  Your script should output: [SENDER],[RECEIVER],[FLAGS]
#  The sender phone number or name (including country code if present)
#  The receiver phone number or name (including country code if present)
#  The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
