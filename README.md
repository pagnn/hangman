# hangman
hangman
实现一个用Python写的单词游戏hangman
一、hangman游戏
Hangman在西方是一个家喻户晓的猜词游戏。Hang的英文意思是“绞死”，而Man的英文意思是“人”。由于竞猜者在规定的猜词次数内没有猜中单词就认为被“绞死”，Hangman便由此而得名。该游戏可以训练竞猜者的反应能力，又可以测试其词汇量。游戏规则如下：计算机随机给出一个单词，用户有八次机会猜测，直到八次机会用完或者猜对游戏结束。
二、Python实现
1.loadWords()，加载words.txt
2.chooseWord(wordlist).,随机产生一个secretword
3.isWordGuessed(secretWord, lettersGuessed)，判断所猜对的字母合集是否能够构成secretword
4.getGuessedWord(secretWord, lettersGuessed)，获取secretword中已经被猜测到的字母
5.getAvailableLetters(lettersGuessed)，获取26个字母中剩下的没被猜测过的字母
6.hangman函数
