package com.example.salaryregression;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText years;
    double[] input = new double[13];
    Button predict;
    double result;
    Model model;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Create an instance of your trained model
        model = new Model();

        // Declare button
        predict = (Button)findViewById(R.id.predict);

        // Declare fields
        years = (EditText)findViewById(R.id.years);

        // Set the button action
        predict.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Make sure there are no empty fields
                if (years.getText().toString().equals("")){
                    // We do not accept empty fields
                    Toast.makeText(MainActivity.this, "Please fill in all input fields.",
                            Toast.LENGTH_LONG).show();
                }
                else{
                    // Get input values
                    input[0] = Double.parseDouble(years.getText().toString());

                    // run the inference
                    result = model.score(input);
                    // show result in a dialog box
                    showResult(String.valueOf(result));
                }
            }
        });

    }
    // method to show the dialog box
    private void showResult(String result) {
        AlertDialog.Builder pred = new AlertDialog.Builder(this);
        pred.setTitle("Inference Result");
        pred.setMessage("Predicted Salary : " + result);
        pred.create().show();
        // clear fields
        years.setText("");
    }
}