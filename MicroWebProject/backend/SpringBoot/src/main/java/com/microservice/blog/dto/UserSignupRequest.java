package com.microservice.blog.dto;

import lombok.Data;

@Data
public class UserSignupRequest {
    private String username;
    private String email;
    private String password;
}

/*

package com.microservice.blog.dto;

public class UserSignupRequest {
    private String email;
    private String username;
    private String password;

    // getter, setter, 생성자 등 추가
}

 */