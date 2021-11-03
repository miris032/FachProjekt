package com.example.test;
/*
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class test {
    public class MainActivity extends AppCompatActivity implements View.OnClickListener {

        Button button1;
        TextView textView1;


        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            button1 = findViewById(R.id.button1);
            textView1 = findViewById(R.id.textView1);


        //1. 第一种点击事件

        //1.1 点击文本框更改文本框内文字
        textView1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textView1.setText("ceshi");
            }
        });


        //1.2 点击按钮更改文本框内文字
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textView1.setText("ceshi");
            }
        });



            //2. 第二种点击事件（最常用）
            button1.setOnClickListener(this);
            textView1.setOnClickListener(this);
        }


        //2. 第二种点击事件（最常用）
        @Override
        public void onClick(View v) {

            int ID = v.getId();

        switch (v.getId()){
            case R.id.button1: textView1.setText("按钮被点击"); break;
            case R.id.textView1: textView1.setText("文本框被点击"); break;
        }

            //if(v.getId() == rando())

        }

        public static int rando(int n){
            int ran = 1;

            if(n == ran){
                return ran;
            }
            return 0;
        }
    }

}
*/