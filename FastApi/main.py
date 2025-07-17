import uvicorn 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
  return {"Hello":"FastAPI"}

if __name__ == "__main__":
  uvicorn.run("main:app",host="127.0.0.1",reload=True)

"""
__name__ == "__main__"의 의미
Python 파일이 실행될 때, 그 파일이 직접 실행된 것인지 아니면 다른 파일에서 import된 것인지에 따라 __name__ 변수의 값이 달라져요.

직접 실행될 경우: __name__은 "__main__"이 됩니다.

다른 파일에서 import될 경우: __name__은 그 파일의 **모듈 이름(파일 이름)**이 됩니다.

예시
# main.py
print(__name__)

$ python main.py
# 출력: __main__

# other.py
import main
bash
복사
편집
$ python other.py
# 출력: main

# if __name__ == "__main__":의 목적
이 조건은 "이 파일이 직접 실행됐을 때만" 실행되게 하고, 다른 모듈에서 import될 때는 실행되지 않도록 하기 위한 거예요.

즉, 이건 **"이 코드는 이 파일이 메인일 때만 실행해"**라는 뜻입니다.

# uvicorn.run("main:app", host="127.0.0.1", reload=True) 이 부분은?
이 줄은 FastAPI 앱을 실행하는 명령인데, 조건문 안에 있기 때문에 main.py를 직접 실행할 때만 실행됩니다.

$ python main.py
이렇게 실행하면:

Python은 main.py를 직접 실행 → __name__ == "__main__"가 참 → uvicorn.run(...) 실행

반대로 main.py를 import해서 쓰는 경우에는 이 코드가 실행되지 않아요.

# 왜 __name__ 값을 바꿀 수 있을까?
실제로 __name__은 Python이 실행 컨텍스트에 따라 자동으로 설정하는 특별한 내장 변수예요. 우리가 직접 바꾸는 게 아니에요.
Python 인터프리터가 이 파일이 직접 실행된 것인지, 아니면 import된 것인지를 감지해서 자동으로 "__main__" 또는 "파일명"으로 설정해요.

요약
__name__ == "__main__" → 이 파일이 직접 실행됐는지 확인하는 방법

uvicorn.run(...)은 그 조건문 안에 있기 때문에 직접 실행할 때만 서버가 실행됨

__name__은 Python이 자동으로 설정해주는 특수 변수

필요하다면 간단한 실험용 코드도 만들어 드릴게요.

> 그럼 __name__ == __main__ 은 수학에서의 정의와 같은 규칙인가?

> __name__ == "__main__"은 마치 수학의 공리처럼 Python 언어 자체의 규칙

# 비유로 이해해 보기
수학에서 "a + b = b + a (교환법칙)" 같은 건 공리 또는 정의에 속하잖아요.
# 왜 그렇냐고 따지기보단 "그렇게 정해졌으니까" 사용하죠.

마찬가지로,

if __name__ == "__main__":
이것도 Python 언어가 그렇게 작동하도록 만들어진 규칙이에요.

🔍 왜 이렇게 설계했을까?
이건 유용함 때문에 의도적으로 설계된 것이에요.

Python은 다음 두 가지 상황을 구분할 필요가 있었어요:

어떤 파일을 직접 실행할 때 → 메인 프로그램

다른 파일에서 import할 때 → 모듈

그래서:

직접 실행 시 __name__은 "__main__"

import 시 __name__은 파일 이름

이걸 활용하면 하나의 Python 파일을:

직접 실행도 가능하고

모듈로 재사용도 가능하게 할 수 있어요

예:
# math_utils.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # 테스트 코드 (직접 실행 시에만 실행)
    print(add(2, 3))  # 5

정리
__name__ == "__main__"은 Python의 내부 규칙이자 언어 설계 철학

수학의 공리처럼, 그 자체로 정의된 규칙이에요

이유보다는 유용성을 위한 설계의 결과
"""