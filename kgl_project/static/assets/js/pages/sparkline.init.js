function hexToRGB(o, i) {
  var l = parseInt(o.slice(1, 3), 16),
    r = parseInt(o.slice(3, 5), 16),
    e = parseInt(o.slice(5, 7), 16);
  return i ? "rgba(" + l + ", " + r + ", " + e + ", " + i + ")" : "rgb(" + l + ", " + r + ", " + e + ")";
}
$(document).ready(function () {
  function i() {
    var o,
      i = ["#6658dd", "#1abc9c"];
    (o = $("#sparkline1").data("colors")) && (i = o.split(",")),
      $("#sparkline1").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40], {
        type: "line",
        width: "100%",
        height: "165",
        chartRangeMax: 50,
        lineColor: i[0],
        fillColor: hexToRGB(i[0], 0.3),
        highlightLineColor: "rgba(0,0,0,.1)",
        highlightSpotColor: "rgba(0,0,0,.2)",
        maxSpotColor: !1,
        minSpotColor: !1,
        spotColor: !1,
        lineWidth: 1,
      }),
      $("#sparkline1").sparkline([25, 23, 26, 24, 25, 32, 30, 24, 19], {
        type: "line",
        width: "100%",
        height: "165",
        chartRangeMax: 40,
        lineColor: i[1],
        fillColor: hexToRGB(i[1], 0.3),
        composite: !0,
        highlightLineColor: "rgba(0,0,0,.1)",
        highlightSpotColor: "rgba(0,0,0,.2)",
        maxSpotColor: !1,
        minSpotColor: !1,
        spotColor: !1,
        lineWidth: 1,
      }),
      (i = ["#4a81d4"]),
      (o = $("#sparkline2").data("colors")) && (i = o.split(",")),
      $("#sparkline2").sparkline([3, 6, 7, 8, 6, 4, 7, 10, 12, 7, 4, 9, 12, 13, 11, 12], { type: "bar", height: "165", barWidth: "10", barSpacing: "3", barColor: i }),
      (i = ["#4fc6e1", "#f7b84b", "#e3eaef", "#f1556c"]),
      (o = $("#sparkline3").data("colors")) && (i = o.split(",")),
      $("#sparkline3").sparkline([20, 40, 30, 10], { type: "pie", width: "165", height: "165", sliceColors: i }),
      (i = ["#2d7bf4", "#4eb7eb"]),
      (o = $("#sparkline4").data("colors")) && (i = o.split(",")),
      $("#sparkline4").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40], {
        type: "line",
        width: "100%",
        height: "165",
        chartRangeMax: 50,
        lineColor: i[0],
        fillColor: "transparent",
        lineWidth: 2,
        highlightLineColor: "rgba(0,0,0,.1)",
        highlightSpotColor: "rgba(0,0,0,.2)",
        maxSpotColor: !1,
        minSpotColor: !1,
        spotColor: !1,
      }),
      $("#sparkline4").sparkline([25, 23, 26, 24, 25, 32, 30, 24, 19], {
        type: "line",
        width: "100%",
        height: "165",
        chartRangeMax: 40,
        lineColor: i[1],
        fillColor: "transparent",
        composite: !0,
        lineWidth: 2,
        maxSpotColor: !1,
        minSpotColor: !1,
        spotColor: !1,
        highlightLineColor: "rgba(0,0,0,1)",
        highlightSpotColor: "rgba(0,0,0,1)",
      }),
      (i = ["#e3eaef", "#6c757d"]),
      (o = $("#sparkline6").data("colors")) && (i = o.split(",")),
      $("#sparkline6").sparkline([3, 6, 7, 8, 6, 4, 7, 10, 12, 7, 4, 9, 12, 13, 11, 12], {
        type: "line",
        width: "100%",
        height: "165",
        lineColor: i[0],
        lineWidth: 2,
        fillColor: "rgba(227,234,239,0.3)",
        highlightLineColor: "rgba(0,0,0,.1)",
        highlightSpotColor: "rgba(0,0,0,.2)",
      }),
      $("#sparkline6").sparkline([3, 6, 7, 8, 6, 4, 7, 10, 12, 7, 4, 9, 12, 13, 11, 12], {
        type: "bar",
        height: "165",
        barWidth: "10",
        barSpacing: "5",
        composite: !0,
        barColor: i[1],
      }),
      (i = ["#36404c"]),
      (o = $("#sparkline7").data("colors")) && (i = o.split(",")),
      $("#sparkline7").sparkline([4, 6, 7, 7, 4, 3, 2, 1, 4, 4, 5, 6, 3, 4, 5, 8, 7, 6, 9, 3, 2, 4, 1, 5, 6, 4, 3, 7], {
        type: "discrete",
        width: "280",
        height: "165",
        lineColor: i,
      }),
      (i = ["#64c5b1", "#5553ce"]),
      (o = $("#sparkline8").data("colors")) && (i = o.split(",")),
      $("#sparkline8").sparkline([10, 12, 12, 9, 7], { type: "bullet", width: "280", height: "80", targetColor: i[0], performanceColor: i[1] }),
      (i = ["#6658dd", "#1abc9c"]),
      (o = $("#sparkline9").data("colors")) && (i = o.split(",")),
      $("#sparkline9").sparkline([4, 27, 34, 52, 54, 59, 61, 68, 78, 82, 85, 87, 91, 93, 100], {
        type: "box",
        width: "280",
        height: "80",
        boxLineColor: i[0],
        boxFillColor: "transparent",
        whiskerColor: i[1],
        medianColor: i[1],
        targetColor: i[1],
      }),
      (i = ["#0acf97", "#e3eaef", "#ff679b"]),
      (o = $("#sparkline10").data("colors")) && (i = o.split(",")),
      $("#sparkline10").sparkline([1, 1, 0, 1, -1, -1, 1, -1, 0, 0, 1, 1], {
        height: "80",
        width: "100%",
        type: "tristate",
        posBarColor: i[0],
        negBarColor: i[1],
        zeroBarColor: i[2],
        barWidth: 8,
        barSpacing: 3,
        zeroAxis: !1,
      });
  }
  function l() {
    var e,
      r = -1,
      t = -1,
      a = 0,
      n = [];
    $("html").mousemove(function (o) {
      var i = o.pageX,
        l = o.pageY;
      -1 < r && (a += Math.max(Math.abs(i - r), Math.abs(l - t))), (r = i), (t = l);
    });
    var p = function () {
      var o = new Date().getTime();
      if (e && e != o) {
        var i = Math.round((a / (o - e)) * 1e3);
        n.push(i), 30 < n.length && n.splice(0, 1), (a = 0);
        var l = ["#f1556c"],
          r = $("#sparkline5").data("colors");
        r && (l = r.split(",")),
          $("#sparkline5").sparkline(n, {
            tooltipSuffix: " pixels per second",
            type: "line",
            width: "100%",
            height: "165",
            chartRangeMax: 77,
            maxSpotColor: !1,
            minSpotColor: !1,
            spotColor: !1,
            lineWidth: 1,
            lineColor: l,
            fillColor: hexToRGB(l[0], 0.3),
            highlightLineColor: "rgba(24,147,126,.1)",
            highlightSpotColor: "rgba(24,147,126,.2)",
          });
      }
      (e = o), setTimeout(p, 500);
    };
    setTimeout(p, 500);
  }
  var r;
  i(),
    l(),
    $(window).resize(function (o) {
      clearTimeout(r),
        (r = setTimeout(function () {
          i(), l();
        }, 300));
    });
});
