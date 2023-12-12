<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<%@ page import="java.io.*" %>

<%
  String sDir      = "";
  String sFileName = "";
  String sFilePath = "";
  String sText     = "";

  String data = request.getParameter("data");
 

  try {

    sDir      = "test";                            // 디렉토리명
    sFileName = "test.txt";                        // 파일명
    sFilePath = sDir + '/' + sFileName;     // 파일경로
   
    // 디렉토리 생성.
    try {
      File dir = new File(sDir);
      dir.mkdirs();
    } catch ( Exception e ) {} 

 

    File sFile = new File(sFilePath);  // file 객체생성
    sFile.createNewFile();    // 파일 생성

 

    //파일쓰기
    FileWriter fw = new FileWriter(sFilePath); // 객체 생성, 같은 이름의 파일명이 있으면 생성안함.

    fw.write(data);  // 파일에 내용 삽입.
    fw.close();
    
}catch(Exception e){
  e.printStackTrace();
}
%>
