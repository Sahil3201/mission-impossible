// $(document).ready(function () {
//     var distance = 120;
//     var time_remaining = $("#time_remaining").val()
//     distance=time_remaining
//     var x = setInterval(function () {
//         distance = distance - 1; ///////////
//         var minutes = Math.floor(distance / 60);
//         var seconds = Math.floor(distance - minutes * 60);
//         document.getElementById("time").innerHTML = ('0' + minutes).slice(-2) + ':' + ('0' + seconds).slice(-2);//minutes + "m " + seconds + "s ";
//         if (distance < 0) {
//             clearInterval(x);
//             document.getElementById("time").innerHTML = "TIME'S UP";
//             document.getElementById("submit").click();
//         }
//     }, 1000);
// })

// $(document).ready(function () {
//     $('#submit').click(function (){
//         event.preventDefault();

//         var q_no = $("#q_no").attr("value");
//         var answer = $("#answer").val();
//         var url = "http://127.0.0.1:8000/quiz/check_ans";
//         $.ajax({
//             type: 'GET',
//             url: url,
//             data: {'answer':answer,'q_no': q_no,},
//             // csrfmiddlewaretoken : '{{ csrf_token }}', },

//             success: function (data) {
//                 myfunc(data);
//             },

//             error: function(data){
//                 alert(data);
//             },
//         });
//         location.reload();
//     });
// })

// function myfunc(data){
//     console.log(data['q_no'],data['que_statement']);
//     // $("#que_no_display").html(data['que_statement'])
//     // document.getElementById("que_no_display").innerHTML = data['que_statement'];
//     $("#que_no_display").html(data['que_statement']);
//     $("#que_statement").html(data['que_statement']);
//     $("#q_no").attr("value",data['q_no']);
//     location.reload();
//     console.log("reload!");
// }
