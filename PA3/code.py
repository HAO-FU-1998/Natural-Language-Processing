import nltk
from nltk import load_parser
from nltk.sem import chat80


def fun1():
    sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
                ("the", "DT"), ("cat", "NN")]
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    print(result)
    result.draw()


def fun3():
    groucho_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> 'in'
    """)
    sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
    parser = nltk.ChartParser(groucho_grammar)
    trees = parser.parse(sent)
    for tree in trees:
        print(tree)


def fun4():
    groucho_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'a' | 'my' | 'the'
    N -> 'park' | 'telescope' | 'man'
    V -> 'saw'
    P -> 'in' | 'with'
    """)
    sent = ['I', 'saw', 'a', 'man', 'with', 'a', 'telescope', 'in', 'the', 'park']
    parser = nltk.ChartParser(groucho_grammar)
    trees = parser.parse(sent)
    for tree in trees:
        print(tree)


def fun5():
    grammar1 = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    P -> "in" | "on" | "by" | "with"
    """)
    sent = "John walked the cat".split()
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    for tree in rd_parser.parse(sent):
        print(tree)


def fun6_7():
    # nltk.data.show_cfg('grammars/book_grammars/sql0.fcfg')
    cp = load_parser('grammars/book_grammars/sql0.fcfg')
    query = 'What cities are located in China'
    trees = list(cp.parse(query.split()))
    answer = trees[0].label()['SEM']
    answer = [s for s in answer if s]
    q = ' '.join(answer)
    print(q)
    rows = chat80.sql_query('corpora/city_database/city.db', q)
    for r in rows:
        print(r[0], end=" ")


def fun8():
    read_expr = nltk.sem.Expression.fromstring
    SnF = read_expr('SnF')
    NotFnS = read_expr('-FnS')
    R = read_expr('SnF -> -FnS')
    prover = nltk.Prover9()
    print(prover.prove(NotFnS, [SnF, R]))


def fun9():
    val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
    dom = set()
    g = nltk.Assignment(dom)
    m = nltk.Model(dom, val)
    print(m.evaluate('(P & Q)', g))
    print(m.evaluate('-(P & Q)', g))
    print(m.evaluate('(P & R)', g))
    print(m.evaluate('(P | R)', g))


def fun10():
    v = """
    bertie => b
    olive => o
    cyril => c
    boy => {b}
    girl => {o}
    dog => {c}
    walk => {o, c}
    see => {(b, o), (c, b), (o, c)}
    """
    val = nltk.Valuation.fromstring(v)
    print(val)


def fun11():
    read_expr = nltk.sem.Expression.fromstring
    a4 = read_expr('exists y. (woman(y) & all x. (man(x) -> love(x,y)))')
    a5 = read_expr('man(adam)')
    a6 = read_expr('woman(eve)')
    g = read_expr('love(adam,eve)')
    mc = nltk.MaceCommand(g, assumptions=[a4, a5, a6])
    print(mc.build_model())


def main():
    fun11()


if __name__ == '__main__':
    main()

