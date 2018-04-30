package com.itstar.util;

import org.w3c.dom.Document;
import org.w3c.dom.Element;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

/**
 * Description:
 *
 * @author heyefu
 * Create in: 2018-02-23
 * Time: 下午8:54
 **/
public class DataDownUtil {

    public static String getHtmlResouceByUrl(String url,String encoding){

        System.out.println("1111");
        String buff = "";
        try {
            //建立网络连接
            URL urlObj = new URL(url);
            //打开网络链接
            URLConnection uc = urlObj.openConnection();
            //文件写入流
            InputStreamReader isr = new InputStreamReader(uc.getInputStream(),encoding);
//            建立文件写入缓冲流
            BufferedReader reader = new BufferedReader(isr);


//            建立临时变量
            String temp = null;

            while ((temp = reader.readLine()) != null){
                buff += temp + "\n";
            }


        } catch (MalformedURLException e) {
            e.printStackTrace();
            System.out.println("网络连接不可用");
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("打开链接失败");
        }

        return buff;
    }


    public static void main(String[] args) {
        System.out.println("test");

        String url = "https://zhidao.baidu.com/question/585856936.html";
        String encoding = "utf-8";
        String html = getHtmlResouceByUrl(url, encoding);
        System.out.println(html);

//        Document document = Jsoup.parse(html);
//        Element element = document.getElementById('hotel_list');
//        Elements elements = element.getElementsByClass('hotel_new_list');




    }
}
