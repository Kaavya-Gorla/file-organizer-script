# My Simple File Organizer

I wrote this quick Python script because my desktop and Downloads folder were getting completely overloaded with random PDFs, images, and zip files. Instead of dragging and dropping everything manually every week, I wanted an automated way to clean it up.

## What it does
- Looks at all the files inside my Downloads folder.
- Checks their file extensions (like `.pdf`, `.png`, `.zip`).
- Automatically creates folders like `Documents` or `Images` if they aren't already there.
- Moves the files into the right folders so everything is neat.
- It completely ignores subfolders so it doesn't accidentally mess up any folders I already made.

## How I run it
I just run it from my terminal whenever things get messy:
```bash
python organizer.py
