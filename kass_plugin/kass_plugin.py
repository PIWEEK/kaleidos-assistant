import os
import pandas as pd
import numpy as np
#
# from webqa import answer_question, PROCESSED_DIR
from mmpy_bot import Bot, Settings
from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message

from webqa import answer_question, PROCESSED_DIR


class KassPlugin(Plugin):
    @listen_to("^.*$")
    async def ai(self, message: Message):
        df = pd.read_csv(f"{PROCESSED_DIR}/embeddings.csv", index_col=0)
        df['embeddings'] = df['embeddings'].apply(eval).apply(np.array)

        print("------")
        print(f"- {message.text}")
        df.head()
        answer = answer_question(
            df,
            question=f"{message.text}",
            max_len=1650,
            max_tokens=1500,
            debug=False
        )
        print(answer)
        self.driver.reply_to(message, answer)




