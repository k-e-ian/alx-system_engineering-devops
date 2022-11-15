#!/usr/bin/env ruby
# regex must be exactly matching string starting with h and ending with n

puts ARGV[0].scan(/^h.n/).join
