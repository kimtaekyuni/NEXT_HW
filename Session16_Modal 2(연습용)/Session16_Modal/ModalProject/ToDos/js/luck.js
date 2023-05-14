const lucks = [
    "오늘은 당신의 날입니다. 인생을 허비하지 마세요."
  ];
  
  const luck = document.querySelector("#luck p");
  const luckToday = lucks[Math.floor(Math.random() * lucks.length)];
  luck.innerText = luckToday;