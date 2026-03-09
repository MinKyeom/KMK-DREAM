// import org.springframework.web.bind.annotation.*;
// import reactor.core.publisher.Flux;
// import reactor.core.publisher.Mono;

// import java.time.Duration;
// import java.util.Arrays;
// import java.util.List;

// @RestController
// @RequestMapping("/books")
// public class WebfluxExample {

//     // 가상의 데이터베이스 대용 데이터
//     private static final List<Book> BOOK_LIST = Arrays.asList(
//         new Book("1", "Spring WebFlux Guide", "Gemini"),
//         new Book("2", "Reactive Programming", "Reactor"),
//         new Book("3", "Java Modern Design", "Oracle")
//     );

//     // 단건 조회: Mono 사용
//     @GetMapping("/{id}")
//     public Mono<Book> getBookById(@PathVariable String id) {
//         return Mono.justOrEmpty(
//             BOOK_LIST.stream()
//                 .filter(book -> book.getId().equals(id))
//                 .findFirst()
//         );
//     }

//     // 전체 조회 (Stream 형태): Flux 사용
//     // delayElements를 주어 비동기 논블로킹의 흐름을 체감할 수 있게 설정했습니다.
//     @GetMapping(value = "", produces = "application/x-ndjson")
//     public Flux<Book> getAllBooks() {
//         return Flux.fromIterable(BOOK_LIST)
//                    .delayElements(Duration.ofMillis(500)); // 0.5초 간격으로 하나씩 방출
//     }
// }