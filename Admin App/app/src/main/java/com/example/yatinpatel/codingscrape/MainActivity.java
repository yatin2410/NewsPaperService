package com.example.yatinpatel.codingscrape;

import android.Manifest;
import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.TimePicker;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Locale;
import java.util.concurrent.TimeUnit;


public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.getName();
    private RequestQueue mRequestQueue;

    private StringRequest stringRequest;
    private String url = "https://shielded-everglades-84549.herokuapp.com/";

    private String[] array = {"sandeshahm","sandeshraj","sandeshbar","sandeshsur","sendnewssandesh","dbahm","dbraj","dbbar","dbsur","sendnewsdb","gsahm","gsraj","gsbar","gssur","sendnewsgs","dabsur","dabdel","sendnewsdab","othertie","otherfe","othertt","othertoi","sendnewsother"};

    public Button button1 ;
    public Button button2;
    public Button button3;
    public Button button4;
    public Button button5;

    public int si;
    public int ej;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        button1 = findViewById(R.id.button);
        button2 = findViewById(R.id.button1);
        button3 = findViewById(R.id.button2);
        button4 = findViewById(R.id.button3);
        button5 = findViewById(R.id.button4);


        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                    makeToast("okay starting");
                    fun1();
            }
        });


        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                makeToast("okay starting");
                fun2();
            }
        });


        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                makeToast("okay starting");
                fun3();
            }
        });



        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                makeToast("okay starting");
                fun4();

            }
        });



        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                makeToast("okay starting");
                fun5();
            }
        });


    }

    private void makeToast(String s) {
        Toast.makeText(MainActivity.this, s,
                Toast.LENGTH_SHORT).show();
    }

private void fun(){
        if (si==ej)
            return;

    Log.d(TAG, "fun: "+si+" "+ej);
    int i = si;
    makeToast("begin " + array[i]);

    mRequestQueue = Volley.newRequestQueue(this);
    stringRequest = new StringRequest(Request.Method.GET, url + array[i], new Response.Listener<String>() {
        @Override
        public void onResponse(String response) {
            makeToast("And Done!!");
            si++;
            fun();
        }

    }, new Response.ErrorListener() {
        @Override
        public void onErrorResponse(VolleyError error) {
            makeToast("Error!!");
            si++;
            fun();
        }
    });

    mRequestQueue.add(stringRequest);
}

    private void fun1() {

        si = 0;
        ej = 5;
        fun();

    }

    private void fun2() {

        si = 10;
        ej = 15;
        fun();

    }

    private void fun3() {

        si = 5;
        ej = 10;
        fun();

    }

    private void fun4() {

        si = 15;
        ej = 18;
        fun();

    }

    private void fun5() {

        si = 18;
        ej = 23;
        fun();

    }


}
