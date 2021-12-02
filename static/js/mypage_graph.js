let orginData = [19959, 21269, 18967, 20476, 21155, 21282, 20440, 21787, 21206, 21123, 21877, 21009, 21301, 21167, 20371, 21084, 21192, 22094, 22340, 23087, 22088, 23305, 22496, 22801, 23181, 22906, 23107, 25515];
let orginLabels = ['2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12', '2021-01', '2021-02', '2021-03']



// 일일 피드 통계량 차트
let daily_statistics = document.getElementById("daily_statistics").getContext('2d');
let daily_chart = new Chart(daily_statistics, {
    type: 'line',
    data: {
        labels: week_labels,
        datasets : [{
            label : '일일 통계량',
            data: week_value,
            borderColor: '#ff4b2b',
        }]
    },
    option: {
    title: {
        display:true,
        text: '일일 피드 통계량'
    }
    }
});


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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});