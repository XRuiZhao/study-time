# Study time

If you study the same subject a few times in a week, this script adds those sessions together. It prints the minutes for each subject and the total for the whole log.

## Try the example

From the project folder, run the following command with Python 3.7 or newer. It uses only the standard library.

```sh
python3 study_time.py example.txt
```

The two Calculus sessions in the example add up to 45 minutes.

```text
Calculus: 45 min
English: 15 min
Total: 60 min
```

## Keep your own log

Create a UTF-8 text file with one session per line. Write the minutes first, then a space and the subject. A name can include spaces, as in `30 Linear algebra`. Use the same spelling each time you log that subject.

Run `python3 study_time.py my-week.txt` with the name of your file. Blank lines are fine, so you can leave a gap between days.
