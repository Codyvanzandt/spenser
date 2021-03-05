# spenser
## A Python package for the works of Edmund Spenser

### TODO
- Ask Steve for (or even better: learn how to get for ourselves) the "easier XML."

- Unit Tests
    - Create some "test xml," structured like just real spenser xml, but smaller.
        - Perhaps just the proem, argument, and first two cantos of book 1 and book 2

- Prepare Book I as a proof of concept
    - Write unit tests for extracting canto numbers against the test xml
    - Extract the canto numbers

    - Write unit tests for extracting stanza numbers against the test xml
    - Extract the stanza numbers

    - Write unit tests for extracting line numbers against the test xml
    - Extract the line numbers

    - Extract the text
        - Write tests for extracting proem text against the test xml
        - Extract the proem text (modern spelling)
        
        - Write tests for extracting argument text against the test xml
        - Extract the argument text (modern spelling)

        - Write tests for extracting poem text against the test xml
        - Extract the poem text (modern spelling)
    
    - Add/extract the title, "The Faerie Queene"
    - Add/extract the book number

    - Write unit tests for formatting the data as a csv
    - Format the data as a CSV, write it to data/xml/

- Prepare all of The Faerie Queene
    - Write unit tests for extracting the book number
    - Extract the book number

- Prepare The Shepheardes Calendar
    - We'll write these todos when we come to them

- Prepare A Theatre for Voluptuous Worldlings
    - We'll write these todos when we come to them

- Prepare the Spenser-Harvey Letters
    - We'll write these todos when we come to them

- Prepare, well, everything else?

- Write examples for use on the project's github site.
- Prettify the project's github site.
    - We'll write these todos when we come to them
- Package up the project and put it on PyPi.
- Advertise the new package!



#### Open Questions
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
