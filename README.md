# spenser
## A Python package for the works of Edmund Spenser

## Useful Knowledge
- How do I run the tests?
    - In a terminal, type: run_tests
- How do I use git and GitHub?
    - git status
    - git add -A
    - git commit -m "Your message"
    - git push

## TODO
- [X] Ask Steve for (or even better: learn how to get for ourselves) the "easier XML."

- Unit Tests
    - [X] Create some "test xml," structured like just real spenser xml, but smaller
        - [X] Perhaps just the proem, argument, and first two stanzas of book 1
    - More unit tests necessary when we get to parsing multiple books of FQ
    - Unit test ensuring we're working with the right edition

- Infrastructure
    - [] Create FQ dataclasses (Why: more readable and logical parsing, plus get a native Python interface for free)
        - [X] line
        - [X] stanza
        - [X] canto
        - [X] book
        - [] text, document, poem -- something like this

- Prepare Book I as a proof of concept
    - [] Write unit tests for parsing the book number
    - [] Parse the book number

    - [] Write unit tests for parsing canto numbers against the test xml
    - [] Parse the canto numbers

    - [] Write unit tests for parsing stanza numbers against the test xml
    - [] parse the stanza numbers

    - [] Write unit tests for parsing line numbers against the test xml
    - [] parse the line numbers

    - [] parse the text
        - [] Write tests for parsing proem text against the test xml
        - [] parse the proem text (modern spelling)
        

        - [] Write tests for parsing argument text against the test xml
        - parse the argument text (modern spelling)

        - [] Write tests for parsing poem text against the test xml
        - parse the poem text (modern spelling)
    
    - [] Add/parse the title, "The Faerie Queene"

    - [] Write unit tests for formatting the data as a csv
    - [] Format the data as a CSV, write it to data/xml/

- [] Prepare all of The Faerie Queene
    - [] Write unit tests for 

- [] Prepare The Shepheardes Calendar
    - [] We'll write these todos when we come to them

- [] Prepare A Theatre for Voluptuous Worldlings
    - [] We'll write these todos when we come to them

- [] Prepare the Spenser-Harvey Letters
    - [] We'll write these todos when we come to them

- [] Prepare, well, everything else?

- [] Write examples for use on the project's github site.
- [] Prettify the project's github site.
    - [] We'll write these todos when we come to them
- [] Package up the project and put it on PyPi.
- [] Advertise the new package!



## Open Questions
- Proems and arguments
    - Where do we put the proems and the arguments?
        - Is a proem "canto 0"?
        - Is an argument "stanza 0"?
- Modern and Oxford Spelling
    - Two top-level packages, modern and oxford, with individual texts underneath?
        - from spenser.oxford import faerie_queen
        - from spenser.modern import faerie_queen
    - Other options?
- Tokenization
    - Should each row contain a line of text?
        - Tokenization is a tricky (and sometimes divisive) task. It feels overly opinionated to force a particular tokenization on users.
    - Or should each row contain an individual token (i.e., word)?
        - Pre-tokenized text is convenient, and the heart of this project is convenience.
- Letters
    - What csv column names should we use for letters?
- Prose Texts
    - What csv column names should we use for prose texts?
- Meta-objects
    - Should we create a csv/dataframe that contains all the poetry?
    - ... all the prose?
    - ... all of Spenser's writing?
    - If so, what csv columns should we use for these meta-objects?
