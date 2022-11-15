#!/usr/bin/env ruby
# regex for patterns, hbtn, hbttn, hbtttn, hbttttn

puts ARGV[0].scan(/hbt+n/).join
