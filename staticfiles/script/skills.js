document.addEventListener("DOMContentLoaded", function () {
    const categoryColors = {
        "data": "#3a0157",       // Data
        "devops": "#570143",     // DevOps
        "programming": "#011230",// Programming
        "web": "#571301"         // Web
    };

    const skillsData = [
        {
            name: "Skills",
            data: skills.map(skill => ({
                name: skill.name,
                value: skill.value,
                color: categoryColors[skill.description] || "#406023"
            }))
        }
    ];

    Highcharts.chart("container1", {
        chart: {
            type: "packedbubble",
            backgroundColor: "transparent",
            animation: {
                duration: 5000
            }
        },
        title: {
            text: null
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        tooltip: {
            enabled: false
        },
        plotOptions: {
            packedbubble: {
                minSize: "30%",
                maxSize: "180%",
                zMin: 0,
                zMax: 150,
                layoutAlgorithm: {
                    gravitationalConstant: 0.001,
                    splitSeries: false,
                    seriesInteraction: true,
                    dragBetweenSeries: true,
                    parentNodeLimit: true
                },
                marker: {
                    fillOpacity: 1,
                    lineWidth: 1,
                    lineColor: "#000"
                },
                dataLabels: {
                    enabled: true,
                    format: "{point.name}",
                    allowOverlap: true,
                    style: {
                        color: "#FDEAEAFF",
                        textOutline: "none",
                        fontWeight: "normal",
                        fontSize: "14px"
                    }
                }
            }
        },
        series: skillsData
    });
});
