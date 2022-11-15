#!/usr/bin/env ruby
# task by professional advisor Neha Jain, Senior Software Engineer at LinkedIn
# regex must match a 10 digit phone number

puts ARGV[0].scan(/^\d{10,10}$/).join
