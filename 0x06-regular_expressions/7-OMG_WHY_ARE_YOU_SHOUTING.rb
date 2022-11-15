#!/usr/bin/env ruby
# regex matching CAPS only

puts ARGV[0].scan(/[A-Z]*/).join
