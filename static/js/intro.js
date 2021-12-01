//Initialize Swiper

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    autoHeight: true,
    centeredSlides: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    loop: true,
    autoplay : {  // 자동 슬라이드 설정 , 비 활성화 시 false
       delay : 3000,   // 시간 설정
       disableOnInteraction : false,  // false로 설정하면 스와이프 후 자동 재생이 비활성화 되지 않음
    },
  });



//chart.js 통계 그래프 
  let feed_sentiment = document.getElementById('feed-sentiment').getContext('2d');
  let sentiment_chart = new Chart(feed_sentiment, {
      type: 'doughnut',
      data: {
          // labels: Object.keys(predicted_value),
          labels: ['부정', '긍정'],
          datasets: [{
              label: '# 긍정',
              data: Object.values(predicted_value),
              backgroundColor: [
                  'rgba(255, 99, 132, 0.8)',
                  'rgba(250, 158, 64, 0.8)',

              ],
              borderColor: [
                  'rgba(255, 99, 132, 0.8)',
                  'rgba(250, 158, 64, 0.8)',
              ],
              borderWidth: 1
              },

      ]
      },
      options: {
          responsive: false,
          plugins:{
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            title:{
              display:true,
              text: "어제 피드 통계"
            }
          }
      }
  });