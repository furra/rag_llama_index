# RAG test implementation with llamaindex.

## Data
https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset/data

## Creating the Database
`sqlite` was used for the db. The database is created alongside a `data/` folder.
```
python create_db.py --help
Usage: create_db.py [OPTIONS]

Options:
  --data_file TEXT  Path to the csv data file.  [required]
  --db_name TEXT    Name of the sqlite database.  [default: database]
  --help            Show this message and exit.
```

## Running the db RAG program
```
python db_rag.py --help
Usage: db_rag.py [OPTIONS]

Options:
  --db_file TEXT  Path to the database file.  [required]
  --help          Show this message and exit.
```

Example:
```
python db_rag.py --db_file data/database.db
Ask anything about the data (CTRL+d to exit):
what's the most purchased item for ages between 30 and 40?
The most purchased item for people aged 30-40 is a backpack, with 43 purchases.

Ask anything about the data (CTRL+d to exit):
What's the average purchase amount for the Winter season that used Bank Transfer as payment method?
There is no data available for average purchase amounts during the Winter season using Bank Transfer as the payment method.

Ask anything about the data (CTRL+d to exit):
For a Size L, what's the most used Payment Method?
For size L, the most used payment method is DEBIT_CARD.
```

## Running the text RAG program
```
python text_rag.py --help
Usage: text_rag.py [OPTIONS]

Options:
  --data_path TEXT  Path where the text files are located.  [required]
  --help            Show this message and exit.

```

Example:
```
python text_rag.py --data_path text/
Ask anything about the texts (enter to exit):
According to the 'In Praise of Difficult Children' text, what does the author say about self-betrayal?
The author posits that adolescents require experimentation with self-betrayal to understand its implications.  This isn't about rule-breaking, but rather breaking personally essential rules, necessitating identification of those rules.  Delinquent behavior is viewed as an unconscious attempt to discover these crucial rules, a frightening process.  Self-betrayal is significant only when it involves betraying oneself; it's a key aspect of adolescence, involving the exploration of self-betrayal and its consequences.  Furthermore, the author notes that  Hamlet considers calling oneself a truant to be self-betrayal, a terrible thing.  Freud suggests that self-betrayal is unavoidable, while Hamlet argues against it.

Ask anything about the texts (enter to exit):
can you sum up the central idea of the third paragraph?
The third paragraph discusses how rules, in addition to their intended purpose, serve as a means of self-discovery.  Breaking rules reveals what rules truly mean and what kind of person one is.  While societal rules are implicitly accepted, adolescence marks a period of questioning and re-evaluating these rules, akin to escaping a restrictive system of belief.

Ask anything about the texts (enter to exit):
what should adults do according to the text?
Adults who care for pre-adolescents must understand what is in the child's best interest, acting as guardians of the child's future self.  They need to be resilient and robust enough to withstand the child's testing behavior, which is crucial for the child to discover whether the adults are trustworthy and dependable.

```
