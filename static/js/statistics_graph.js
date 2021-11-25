// 환자수 추이 chart
let orginData = [19959, 21269, 18967, 20476, 21155, 21282, 20440, 21787, 21206, 21123, 21877, 21009, 21301, 21167, 20371, 21084, 21192, 22094, 22340, 23087, 22088, 23305, 22496, 22801, 23181, 22906, 23107, 25515];
let orginLabels = ['2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03']

let patient = document.getElementById("patient").getContext('2d');
let patientChart = new Chart(patient, {
    type: 'line',
    data: {
        labels: orginLabels,
        datasets : [{
            label : '환자수',
            data: orginData,
            borderColor: '#ff4b2b',
        }]
    },
    options: {
        plugins: {
            title: {
                display:true,
                text: '외래/입원환자 수 추이'
            }
        }
    }
});

// 성별/연령 chart
let sexAge1 = document.getElementById('sexAge1').getContext('2d');
let sexAge_bar_chart = new Chart(sexAge1, {
  type: 'bar',
  data: {
      labels: ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80'],
      datasets: [{
          label: '# 남',
          data: [546, 6011, 18042, 20700, 27062, 32072, 34357, 27264, 12544],
          backgroundColor: [
              'rgba(54, 162, 235, 0.5)'
          ],
          borderColor: [
              'rgba(90, 162, 235, 1)',
          ],
          borderWidth: 1
          },
          {
          label: '# 여',
          data: [588, 6756, 25570, 28566, 37396, 50134, 65740, 51063, 25028],
          backgroundColor: [
              'rgba(255, 99, 132, 0.5)'
              
          ],
          borderColor: [
              'rgba(255, 99, 132, 1)'
          ],
          borderWidth: 1
        }
    ]
    },
    options: {
        plugins: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            title: {
                display:true,
                text: '성별별 코로나 블루 특성'
            }
        
        }
    }
});
let sexAge2 = document.getElementById('sexAge2').getContext('2d');
let sexAge_pie_chart = new Chart(sexAge2, {
    type: 'doughnut',
    data: {
        labels: ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80'],
        datasets: [{
            label: '# 남',
            data: [90415, 905522, 2794352, 2868808, 3285230, 3772975, 4333064, 3156063, 1448510],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(250, 158, 64, 0.5)',
                'rgba(252, 205, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(90, 100, 235, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(193, 132, 255, 0.5)',
                'rgba(201, 203, 207, 0.5)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(250, 158, 64, 0.5)',
                'rgba(252, 205, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(201, 203, 207, 0.5)',
                'rgba(90, 100, 235, 0.5)'
            ],
            borderWidth: 1
            },
            
    ]
    },
    options: {
        plugins:{
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    }
});

// 긍부정 누적 chart
let total_keyword = document.getElementById("total_keyword").getContext('2d');
let totalKeywordChart = new Chart(total_keyword, {
    type: 'bar',
    data: {
        labels: orginLabels,
        datasets : [{
            label : '긍정',
            data: orginData,
            borderColor: '#',
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
        },
        {
            label : '부정',
            data: orginData,
            borderColor: '#ff4b2b',
            backgroundColor: 'rgba(255, 99, 132, 1)'
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: '긍/부정'
            },
        },
        responsive: true,
        // scales: {
        //     x: {
        //         stacked: true,
        //     },
        //     y: {
        //         stacked: true
        //     }
        // }
    }
});


let naver_sentiment = document.getElementById("naver_sentiment").getContext('2d');
let naverKeywordChart = new Chart(naver_sentiment, {
    type: 'bar',
    data: {
        labels: orginLabels,
        datasets : [{
            label : '긍정',
            data: orginData,
            borderColor: '#',
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
        },
        {
            label : '부정',
            data: orginData,
            borderColor: '#ff4b2b',
            backgroundColor: 'rgba(255, 99, 132, 1)'
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Chart.js Bar Chart - Stacked'
            },
        },
        responsive: true,
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true
            }
        }
    }
});

let twitter_sentiment = document.getElementById("twitter_sentiment").getContext('2d')
let twitterKeywordChart = new Chart(twitter_sentiment, {
    type: 'bar',
    data: {
        labels: orginLabels,
        datasets : [{
            label : '긍정',
            data: orginData,
            borderColor: 'rgba(54, 162, 235, 0.5)',
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
        },
        {
            label : '부정',
            data: orginData,
            borderColor: 'rgba(54, 162, 235, 0.5)',
            backgroundColor: 'rgba(255, 99, 132, 1)'
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Chart.js Bar Chart - Stacked'
            },
        },
        responsive: true,
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true
            }
        }
    }
});


