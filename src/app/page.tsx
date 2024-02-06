import { H1 } from "@/components/ui/H1";
import { Metadata } from "next";
import Image from "next/image";
import me from "@/assets/me.jpg";
import { H2 } from "@/components/ui/H2";
import { Bot } from "lucide-react";

export const metadata: Metadata = {
  title: "Fredrick Bernard - Portfolio",
};

export default function Home() {
  return (
    <section className="space-y-16 bg-[url('/background.png')] bg-cover bg-center bg-no-repeat px-1 py-8">
      <section className="grid grid-cols-1 items-center gap-8 sm:grid-cols-2">
        <div className="space-y-3">
          <H1 className="text-center sm:text-start">Hi, I&apos;m Bernard 👋</H1>
          <p className="text-left sm:text-start">
            I&apos;m passionate full-stack developer who thrives on creating
            innovative and user-centric projects. With a keen eye for detail and
            a strong foundation in both front-end and back-end technologies, I
            specialize in bringing ideas to life through code.
          </p>
        </div>
        <div className="flex justify-center">
          <Image
            src={me}
            alt={" of me"}
            height={300}
            width={300}
            className="aspect-square rounded-full border-2 object-cover shadow-md dark:border-foreground"
          />
        </div>
      </section>
      <section className="space-y-3 text-center">
        <H2>Ask the chatbot anything about me.</H2>
        <p>
          Click the little <Bot className="inline pb-1"/> icon in the top bar
          to activate the AI chat. You can ask the chatbot anyquestion about me
          and it will find relevant info on this website. The bot can even provide links
          to pages you&apos;re looking for.
        </p>

      </section>
    </section>
  );
}
