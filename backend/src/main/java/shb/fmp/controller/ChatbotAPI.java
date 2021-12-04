package shb.fmp.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChatbotAPI {

    @RequestMapping(value = "/chatbot")
    public String getChatting() {

        return "test";
    }
}
