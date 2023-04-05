#!/usr/bin/ruby

require 'rbygem'
require 'mongo'

$client = Mongo::Client.new(['127.0.0.1:27017'], :database => 'test')
Mongo::Logger.logger.level = ::Logger::ERROR
$users = $client[:users]
puts 'connected!'

cursor = $users.find()
cursor.each do | doc |
    puts doc
end

# json이 아닌 bson으로 들어간다 이렇게 넣으면 