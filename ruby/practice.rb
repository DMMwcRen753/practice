def create_number(number)
  number_list = []
  for i in 1.upto(number) do
    if (i % 7 == 0 )
      number_list.append(i)
    end
  end
  return number_list.sum{|i| i.to_s.count("7")}
  # return number_list
end

puts "#{create_number(7777777)}"