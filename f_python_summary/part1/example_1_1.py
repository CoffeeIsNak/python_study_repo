# Pythonic card deck
# __getitem__, __len__ 관련 실습 코드

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()

# 1. FreanchDeck 객체는 __len__ 메소드에 의해 길이 제공
print(f"length of deck: {len(deck)}")  # 52

# 2. FrenchDeck 객체는 __getitem__ 메소드로 인해 특정 위치의 데이터에 접근 가능, 슬라이싱도 가능
print(f"first card: {deck[0]}")  # Card(rank='2', suit='spades')
print(f"last card: {deck[-1]}")  # Card(rank='A', suit='hearts')
print(f"first three cards: {deck[:3]}")  # [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
print(f"all aces: {deck[12::13]}")  # [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

# 3. 랜덤한 카드를 고르고 싶을 때 => 메소드 구현 필요 X. 이미 파이썬이 제공함
from random import choice
print(f"random choice for card: {choice(deck)}")  # 매번 다른 객체를 뽑음 => Card(rank='3', suit='diamonds')

# 4. FrenchDeck 객체는 __getitem__ 메소드로 인해 for문에서도 활용 가능함. reversed도 가능함
for i, card in enumerate(deck):
    print(f"{i + 1}th card: {card}")

for i, card in enumerate(reversed(deck)):
    print(f"reversed order {i + 1}th card: {card}")

# 5. collection에 __contins__ 메소드가 없으면 in 연산자는 sequential scan을 한다
print(Card('Q', 'hearts') in deck)  # True
print(Card('Q', 'coffee') in deck)  # False

# 6. 정렬에는 아래와 같은 함수를 이용할 수 있다. => 아래 함수는 2클로버에 0, 스페이드 에이스에 51을 반환 
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# 함수를 이용하여 정렬
for card in sorted(deck, key=spades_high):
    print(f"sorted {i + 1}th card: {card}")
