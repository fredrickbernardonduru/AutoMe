import Link from "next/link";
import ThemeToggle from "../ThemeToggle";
import AIChatButton from "../AIChatButton";

export default function Navbar() {
  return (
    <header className="sticky top-0 bg-background">
      <div className="gap3 mx-auto flex max-w-3xl flex-wrap justify-between px-4 py-3">
        <nav className="space-x-4 font-medium">
          <Link href="/">Home</Link>
          <Link href="/about">About me</Link>
          <Link href="/social">Social media</Link>
        </nav>
        <div className="flex items-center gap-4">
          <AIChatButton />
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
}
