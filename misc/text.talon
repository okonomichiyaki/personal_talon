
clear left <number_small> words:
    edit.extend_word_left()
    repeat(number_small - 1)
    edit.delete()
clear right <number_small> words:
    edit.extend_word_right()
    repeat(number_small - 1)
    edit.delete()
clear left <number_small> characters:
    edit.extend_left()
    repeat(number_small - 1)
    edit.delete()
clear right <number_small> characters:
    edit.extend_right()
    repeat(number_small - 1)
    edit.delete()

inside singles:
	insert("''")
	key(left)
inside angles:
	insert("<>")
	key(left)

trip: "t"
blank: " "
bar: " "
slam: key(enter)
sloop:
    edit.line_start()
    key(enter)
    edit.up()

dupe line:
    edit.select_line()
    edit.copy()
    edit.paste()

say colon: ";"

clear line:
  key(delete)
