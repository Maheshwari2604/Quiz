navigator.getUserMedia = navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia;

if (navigator.getUserMedia) {
   navigator.getUserMedia({ audio: true, video: { width: 1280, height: 720 } },
      function(stream) {
         var video = document.querySelector('video');
         video.srcObject = stream;
         video.onloadedmetadata = function(e) {
           video.play();
         };
      },
      function(err) {
         console.log("The following error occurred: " + err.name);
      }
   );
} else {
   console.log("getUserMedia not supported");
}

// if (navigator.getUserMedia) {
//    navigator.getUserMedia({ video: true })
//      .then(function (stream) {
//        video.srcObject = stream;
//      })
//      .catch(function (err0r) {
//        console.log("Something went wrong!");
//      });
//  }
//  /FileStore/tables/Sacramentorealestatetransactions.csv