#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()
print('Content-type: text/html\n')
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<body><table><tr><td><h1>You guessed:</h1><img src=cards/{cardimg}></td></tr><tr><td><h1>Suit:</h1>{cardsuit}</td><tr><td><h1>Rank:</h1>{cardrank}</td>
</tr></table>
</form>
</body></html>
"""
extra= """<form method="post" action="guessmycard.cgi">
	<H2>Try to guess the card!</H2>
	<p>Rank:
		<select name="rank">
			<option>2</option>
			<option>3</option>
			<option>4</option>
			<option>5</option>
			<option>6</option>
			<option>7</option>
			<option>8</option>
			<option>9</option>
			<option>10</option>
			<option>J</option>
			<option>Q</option>
			<option>K</option>
			<option>A</option>
		</select>
	</p>
	<p>Suit:
		<br /><input type="radio" name="suit" value="C" />Clubs
		<br /><input type="radio" name="suit" value="D" />Diamonds
		<br /><input type="radio" name="suit" value="H" />Hearts
		<br /><input type="radio" name="suit" value="S" />Spades
	</p>
	<button type="submit">Submit</button>"""
form = cgi.FieldStorage()
cardNum =form.getfirst("rank","2")
cardSuit= form.getfirst("suit","C")
highcard=["A","K","J","Q"]
inputN="10"
inputS="S"

cN=""
if cardNum == inputN:
    cN+="Correct Card Number"
else:
    cN+="Not Correct"
    if cardNum in highcard:
        cN+="Card to High"
    else:
        cN+="Card to Low"
cS=""
if cardSuit == inputS:
    cS+="Card suit right"
else:
    cS+="Card suit wrong"
if cardSuit !=inputS or cardNum!=inputN:
    cN+= extra
elif cardSuit !=inputS or cardNum!=inputN:
    cN+= extra
else:
    cN+=" "

cI=""
cI+= cardNum+cardSuit+".jpg"
print(html.format(cardimg= cI, cardsuit=cS, cardrank= cN))
