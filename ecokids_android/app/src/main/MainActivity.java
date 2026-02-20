package com.terrence.ecokids;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings;

public class MainActivity extends Activity {
    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Configuración de Pantalla Completa Elite
        mWebView = new WebView(this);
        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        
        mWebView.setWebViewClient(new WebViewClient());
        
        // Conexión Directa al Servidor de Terrence Mayorga
        mWebView.loadUrl("https://terrence-m-ecokids.onrender.com");
        
        setContentView(mWebView);
    }
}
