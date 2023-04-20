import pandas as pd
import numpy as np

from webqa import answer_question, PROCESSED_DIR

df = pd.read_csv(f"{PROCESSED_DIR}/embeddings.csv", index_col=0)
df['embeddings'] = df['embeddings'].apply(eval).apply(np.array)

df.head()

answer = lambda question: print(answer_question(df, question=f"{str(question)}",  max_len=1650, max_tokens=1500, debug=False))
