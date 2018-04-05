# CSC405-SwampCTF-OrbOfLight1
Attempt to solve Orb of Light 1 from SwampCTF

I started off with using https://www.guballa.de/substitution-solver to have something to work with. From there, I could make out some of the words in the estimated decrypted text and started manually creating a dictionary script based on the letters that I replaced to obtain English words (see decode.py for the dictionary). After manually creating all of the known dictionary, I ended up with the decoded message.

The message is decoded but I have no idea of what the flag is. I tried a few possibilities such as encoding and decoding "flag" or "secret". I am not sure of how to proceed. The encoding and decoding scripts with the known dictionary are attached. Run from some CLI using Python 3.

- Ruben (rabaraho@ncsu.edu)

From secret_message_decoded.txt:

```
Dominion of shadows and unusual things

"Toxic domain of dark illusion
Land that shrouds loathing light
boundary of worlds unknown"

Land of shadows, a twilight domain that is a dark mirror, or copy, of you world. a point of blight and corrosion, a domain out of sync, a land with horrors right by you and you don’t know.

Artisans of a thaumaturgical kind do not usually cross into lands of shadow for in such domains an unknown horror is said to lurk.  Arrival always brings about dissolution of aspirations for shadows quickly swallow souls of light in a mystic impossibility.  A solitary augury was proof: Kingdoms will fall as conjuration of shadow glooms midday with dark malicious fog, a luminous charm will cast a ray that again aligns our world.
```
