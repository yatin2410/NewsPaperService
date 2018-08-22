(function() {
   
  // Initialize Firebase


    //Get elements

    const btnLogOut = document.getElementById('btnlo');
    const subt = document.getElementById('subt');  
    var isexisted = false;
    var key;

   btnLogOut.addEventListener('click', e => {
        firebase.auth().signOut();
    });

    //Add a realtime listener
    firebase.auth().onAuthStateChanged(firebaseUser =>{

        if(firebaseUser)
        {
            var firebaseRef = firebase.database().ref();
            var email = firebaseUser.email.toString();
            var arr = document.getElementsByTagName('input');                

        firebaseRef.child('news').orderByChild('email').equalTo(email).on("value", function(snapshot) {
        console.log(snapshot.val());
        snapshot.forEach(function(data) {
        isexisted = true;
        key = data.key;
        console.log(snapshot.val()[data.key].sub);
        var array = snapshot.val()[data.key].sub.split(' ');
        for(var i=0;i<arr.length;i++)
                {
                    for(var j=0;j<array.length;j++)
                    {
                    if(arr[i].value==array[j])
                    {
                        arr[i].checked = true;
                    }
                }

                }
        });
    });

        subt.addEventListener('click',e => { 

                var str = "";
                for(var i=0;i<arr.length;i++)
                {
                    if(arr[i].checked)
                    {
                        str += arr[i].value+" ";
                    }
                }
                console.log(isexisted);
                if(!isexisted)
                  firebaseRef.child('news').push({email:email,sub:str});
                else
                {
                    console.log(key);
                    firebaseRef.child('news').child(key).remove();
                    firebaseRef.child('news').push({email:email,sub:str});
                }
                window.alert('And Done!! Told you just a click!');

             });

            console.log(firebaseUser);

        }

        else
        {
            console.log('not logged in');
            document.location.href = 'index.html';
        }

    });

}());

