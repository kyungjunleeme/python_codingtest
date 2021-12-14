# python_codingtest
시니어 개발자분의 조언을 듣고 하루에 한 개씩 파이썬 코딩 문제를 풀겠다는 목표로 해당 repo를 만들게되었습니다.


https://www.youtube.com/watch?v=5Lu34WIx2Us


트리구조 - 인덱스 공부하다가

Django on Python does well in agile web development. Python is dynamic programming language, as is known, its runtime efficiency is low. the question is how it will affect Django's efficiency. This Paper answered the question from the angle of memory optimization, by improving the efficiency of Python in memory use, we will see how it will affect django. Python manages non-container objects with the technology of memory pool, after a consequence of allocate and free operations, it will produce memory fragment, and the garbage collection module can hardly handle it. This paper proposed a new non-container object management greedy algorithm, it can minimize the probability of generating fragments, thus the garbage collection module can collect garbage non-container objects in time. We conduct our experiment on the benchmark of an open-source project named Unladen-Swallow. When Django renders a template, it will save about 10% memory, with almost the same time consuming.


와 내가 공부해야하는 개념을 제대로 설명해주고 있다.

https://www.researchgate.net/publication/271547188_A_Method_of_Optimizing_Django_Based_on_Greedy_Strategy


