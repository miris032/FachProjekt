package com.example.test;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;


public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Button button1;
    TextView textView1;
    EditText editText1;

    int key = 0;
    int num = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button1 = findViewById(R.id.start1);
        textView1 = findViewById(R.id.title1);
        editText1 = findViewById(R.id.eingabe);

        button1.setOnClickListener(this);
        textView1.setOnClickListener(this);
        editText1.setOnClickListener(this);
    }


    @Override
    public void onClick(View v) {



        if (v.getId() == R.id.start1) {
            int input = Integer.parseInt(editText1.getText().toString().trim());
            int random = getRandom();

            if(key == 0){
                num = random;
            }

            if(button1.getText() == "重新开始"){

                button1.setText("Start");
            }

            if(input == num){
                textView1.setText("猜对了！");

                //进入下一轮
                button1.setText("重新开始");
                editText1.setText(null);
                key = 0;
            }
            else{
                if(input < num){
                    textView1.setText("猜小了，继续猜");
                    editText1.setText(null);
                    key = 1;
                }
                else{
                    textView1.setText("猜大了，继续猜");
                    editText1.setText(null);
                    key = 1;
                }
            }
        }
    }




    public int getRandom() {

        //随机数范围
        int min = 1; int max = 10;
        int n = (int)(Math.random() * max) + min;

        return n;
    }






}