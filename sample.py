{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e7003b11-b25f-4f20-8221-2374f38b868f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl.metadata (20 kB)\n",
      "Requirement already satisfied: flask in c:\\programdata\\anaconda3\\lib\\site-packages (3.0.3)\n",
      "Collecting twilio\n",
      "  Downloading twilio-9.3.7-py2.py3-none-any.whl.metadata (12 kB)\n",
      "Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (3.0.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from flask) (1.6.2)\n",
      "Requirement already satisfied: requests>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from twilio) (2.32.3)\n",
      "Requirement already satisfied: PyJWT<3.0.0,>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from twilio) (2.8.0)\n",
      "Requirement already satisfied: aiohttp>=3.8.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from twilio) (3.10.5)\n",
      "Collecting aiohttp-retry==2.8.3 (from twilio)\n",
      "  Downloading aiohttp_retry-2.8.3-py3-none-any.whl.metadata (8.9 kB)\n",
      "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (2.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (23.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (1.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from aiohttp>=3.8.4->twilio) (1.11.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.0.0->twilio) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.0.0->twilio) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.0.0->twilio) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests>=2.0.0->twilio) (2024.8.30)\n",
      "Downloading opencv_python-4.10.0.84-cp37-abi3-win_amd64.whl (38.8 MB)\n",
      "   ---------------------------------------- 0.0/38.8 MB ? eta -:--:--\n",
      "   - -------------------------------------- 1.8/38.8 MB 10.1 MB/s eta 0:00:04\n",
      "   ---- ----------------------------------- 3.9/38.8 MB 9.8 MB/s eta 0:00:04\n",
      "   ----- ---------------------------------- 5.2/38.8 MB 8.6 MB/s eta 0:00:04\n",
      "   ------- -------------------------------- 7.1/38.8 MB 8.9 MB/s eta 0:00:04\n",
      "   -------- ------------------------------- 8.7/38.8 MB 8.4 MB/s eta 0:00:04\n",
      "   --------- ------------------------------ 9.2/38.8 MB 7.8 MB/s eta 0:00:04\n",
      "   ---------- ----------------------------- 10.5/38.8 MB 7.3 MB/s eta 0:00:04\n",
      "   ----------- ---------------------------- 11.5/38.8 MB 7.1 MB/s eta 0:00:04\n",
      "   ------------- -------------------------- 12.8/38.8 MB 6.9 MB/s eta 0:00:04\n",
      "   -------------- ------------------------- 14.2/38.8 MB 7.1 MB/s eta 0:00:04\n",
      "   ---------------- ----------------------- 16.0/38.8 MB 7.1 MB/s eta 0:00:04\n",
      "   ------------------ --------------------- 17.8/38.8 MB 7.3 MB/s eta 0:00:03\n",
      "   ------------------- -------------------- 19.4/38.8 MB 7.3 MB/s eta 0:00:03\n",
      "   --------------------- ------------------ 20.7/38.8 MB 7.3 MB/s eta 0:00:03\n",
      "   ----------------------- ---------------- 22.5/38.8 MB 7.4 MB/s eta 0:00:03\n",
      "   ------------------------- -------------- 24.6/38.8 MB 7.6 MB/s eta 0:00:02\n",
      "   --------------------------- ------------ 26.5/38.8 MB 7.7 MB/s eta 0:00:02\n",
      "   ---------------------------- ----------- 28.0/38.8 MB 7.7 MB/s eta 0:00:02\n",
      "   ------------------------------- -------- 30.1/38.8 MB 7.8 MB/s eta 0:00:02\n",
      "   -------------------------------- ------- 32.0/38.8 MB 7.8 MB/s eta 0:00:01\n",
      "   ---------------------------------- ----- 33.8/38.8 MB 8.0 MB/s eta 0:00:01\n",
      "   ------------------------------------ --- 35.1/38.8 MB 7.8 MB/s eta 0:00:01\n",
      "   -------------------------------------- - 37.2/38.8 MB 7.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 38.8/38.8 MB 7.9 MB/s eta 0:00:00\n",
      "Downloading twilio-9.3.7-py2.py3-none-any.whl (1.8 MB)\n",
      "   ---------------------------------------- 0.0/1.8 MB ? eta -:--:--\n",
      "   ---------------------------------- ----- 1.6/1.8 MB 7.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.8/1.8 MB 7.1 MB/s eta 0:00:00\n",
      "Downloading aiohttp_retry-2.8.3-py3-none-any.whl (9.8 kB)\n",
      "Installing collected packages: opencv-python, aiohttp-retry, twilio\n",
      "Successfully installed aiohttp-retry-2.8.3 opencv-python-4.10.0.84 twilio-9.3.7\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install opencv-python flask twilio numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2be5e04-ffa8-4916-9f81-bf8d677b7478",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
