// patient
// const patient = document.getElementById('patient').getContext('2d');
const count = document.getElementById('count').getContext('2d');

// sex/age
const sexAge = document.getElementById('sexAge').getContext('2d');
const sexAge2 = document.getElementById('sexAge2').getContext('2d');

// region
const temp1 = document.getElementById('temp1').getContext('2d');
const temp2 = document.getElementById('temp2').getContext('2d');
const temp3 = document.getElementById('temp3').getContext('2d');



// draw chart
// const patientGraph = new Chart(patient, {
//     type: 'line',
//     data: {
//         labels: ['2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6'],
//         datasets: [{
//             label: 'F41.1',
//             data: [9, 13, 23, 19, 21, 35],
//             backgroundColor: [
//                 'rgba(54, 162, 235, 0.5)'
//             ],
//             borderColor: [
//                 'rgba(90, 162, 235, 1)',
//             ],
//             borderWidth: 1
//             },
//             {
//             label: 'F41.9',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.5)'
                
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)'
//             ],
//             borderWidth: 1
//         }
//     ]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             }
//         }
//     }
// });

const countGraph = new Chart(count, {
    type: 'line',
    data: {
        labels: ['2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6'],
        datasets: [{
            label: 'F41.1',
            data: [9, 13, 23, 19, 21, 35],
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)'
            ],
            borderColor: [
                'rgba(90, 162, 235, 1)',
            ],
            borderWidth: 1
            },
            {
            label: 'F41.9',
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const sexAgeGraph = new Chart(sexAge, {
    type: 'bar',
    data: {
        labels: ['10대', '20대', '30대', '40대', '50대', '60대'],
        datasets: [{
            label: '# 남',
            data: [9, 20, 2, 8, 5, 7],
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
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const sexAgeGraph2 = new Chart(sexAge2, {
    type: 'bar',
    data: {
        labels: ['10대', '20대', '30대', '40대', '50대', '60대'],
        datasets: [{
            label: '# 남',
            data: [9, 20, 2, 8, 5, 7],
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
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


const temp1Graph = new Chart(temp1, {
    type: 'pie',
    data: {
        labels: ['10대', '20대', '30대', '40대', '50대', '60대'],
        datasets: [{
            label: '# 남',
            data: [9, 20, 2, 8, 5, 7],
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
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const temp2Graph = new Chart(temp2, {
    type: 'line',
    data: {
        labels: ['10대', '20대', '30대', '40대', '50대', '60대'],
        datasets: [{
            label: '# 남',
            data: [9, 20, 2, 8, 5, 7],
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
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const temp3Graph = new Chart(temp3, {
    type: 'bar',
    data: {
        labels: ['10대', '20대', '30대', '40대', '50대', '60대'],
        datasets: [{
            label: '# 남',
            data: [9, 20, 2, 8, 5, 7],
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
            data: [12, 19, 3, 5, 2, 3],
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});