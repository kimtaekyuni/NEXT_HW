const dc = document; //document 너무 기니까 dc로 줄여보기
const body = dc.body; //매번 dc.body 치기 귀찮으니까 body로 줄여보기
const container = dc.createElement("div"); //createElement로 div 요소 생성, container로 명

container.innerText = "메인 컨테이너"; //새로 생성한 div 즉 container의 내부 Text를 "메인 컨테
container.classList.add("container");//새로 생성한 div 즉 container의 class에 "container" 

const title = dc.createElement('h1');//createElement로 h1 요소 생성, title로 명명
title.innerText = "타이틀"; //새로 생성한 h1 즉 title의 내부 Text를 "타이틀"로 쓰기
title.classList.add('title'); //새로 생성한 h1 즉 title의 class에 "title" 추가하기

body.append(container); //document.body 밑에 container을 추가
container.append(title); 