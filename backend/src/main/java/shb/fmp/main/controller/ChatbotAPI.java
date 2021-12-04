package shb.fmp.main.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChatbotAPI {

    @GetMapping(value = "/chatbot")
    public String getChatting() {
        System.out.println("test");
        return "test";
    }
}
