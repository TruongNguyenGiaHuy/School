def game_play():
  s1=randnum()
  s2=randnum()
  dbscore=False
  if s1==s2:
    dbscore=True
  sum=s1+s2
  print(f"You rolled {s1} and {s2}, your total score is {sum}")
  while True:
    if(yes_no("Do you want to continue rolling the dice? ")):
      temp=randnum()
      sum=sum+temp
      print("\n"+"\n"+f"You rolled {temp}"+"\n"+f"Your total score is now {sum}")
    else:
      return sum , dbscore
playerscore , db = game_play()
print(playerscore + db)
