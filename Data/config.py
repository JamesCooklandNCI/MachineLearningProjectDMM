dataCleansing = {"mentions" : r"@([a-zA-z0-9]+)",
                 "hashtags" : r"#([a-zA-z0-9]+)",
                 "tags": r"<br />",
                 "whiteSpace" : r"[^\w\s+]",
                 "URL" : r"^https?:\/\/.*[\r\n]*",
                 "numbers" : r"\d+",
                 "newLines" : r"\n",
                 "duplicateChars" : "r(.)\1+"}


                 